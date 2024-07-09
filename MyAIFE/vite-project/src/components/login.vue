<template>
  <el-form
    ref="ruleFormRef"
    style="max-width: 600px"
    :model="ruleForm"
    status-icon
    :rules="rules"
    label-width="auto"
    class="demo-ruleForm"
  >
    <el-form-item label="账号" prop="user">
      <el-input
        v-model="ruleForm.username"
        type="username"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item label="密码" prop="pass">
      <el-input
        v-model="ruleForm.password"
        type="password"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)">
        提交
      </el-button>
      <el-button @click="resetForm(ruleFormRef)">重置</el-button>
    </el-form-item>
  </el-form>
</template>
  
  <script lang="ts" setup>
import { reactive, ref } from "vue";
import  {
  FormInstance,
  FormRules,
  ElMessage,
  ElNotification,
} from "element-plus";
import axios from "axios";
import { useRoute,useRouter } from 'vue-router'

const router = useRouter(); //路由
const ruleFormRef = ref(); //校验规则

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Please input the password"));
  } else {
    if (ruleForm.password !== "") {
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkPass");
    }
    callback();
  }
};
const validateUser = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Please input the username"));
  } else {
    if (ruleForm.username !== "") {
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkPass");
    }
    callback();
  }
};
const ruleForm = reactive({
  password: "",
  username: "",
});

const rules = reactive({
  pass: [{ validator: validatePass, trigger: "blur" }],
  user: [{ validator: validateUser, trigger: "blur" }],
});

const baseUrl = "http://127.0.0.1:8000/";
const submitForm = (formEl) => {
  console.log(formEl, "infos");
  console.log(localStorage,'local')
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      submitUserPass();
      console.log("submit!");
    } else {
      console.log("error submit!");
    }
  });
};

function submitUserPass() {
  console.log("地址", baseUrl + "users/login/");
  axios
    .post(baseUrl + "users/login/", ruleForm, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((res) => {
      if (res.data.code === 1) {
        // console.log(res.data)
        localStorage.setItem("token",res.data.data.token)
        ElNotification.success({
          title: "Info",
          message: "登录成功",
          showClose: false,
        });
        router.push('/')
      } else {
        ElNotification.error({
          title: "Info",
          message: "登录失败",
          showClose: false,
        });
      }
    })
    .catch((err) => {
      console.log("失败", err);
    });
}
const resetForm = (formEl) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>
  