
<template>
    <div class="common-layout">
      <el-container>
        <el-header>
            <div></div>
            <el-button class="logout_button" @click="logout">退出</el-button>
        </el-header>
        <el-container>

            <asideMenu @menu-event="updateMenuMessage"></asideMenu>
          <el-container>
            <el-main>
              <!-- <mymain ></mymain> -->
              <!-- <myalgorithm v-if="menuMessage=='1-1'">33</myalgorithm>
              <myvideo v-if="menuMessage=='2-1'"></myvideo> -->
              <component :is="store.state.mainPage"></component>
            </el-main>
            <el-footer>Footer</el-footer>
          </el-container>
        </el-container>
      </el-container>
    </div>
  </template>


<script setup>
import { useRoute,useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { defineComponent, ref,shallowRef,computed, onMounted } from 'vue'
import asideMenu from './Menu.vue'
import mymain from './mymain.vue'
import myvideo from './myvideo.vue'
import myalgorithm from './myalgorithm.vue'
import mydeploy from './mydeploy.vue'
import myvideiomanager from './myvideoManager.vue'
const store = useStore()
const logout = ()=>{store.commit("logout")}
const router = useRouter(); //路由
// const chosecomponent = shallowRef(mymain)

store.state.mainPage = mymain

const menuMessage = ref('3-1')
//子组件菜单更新值
const updateMenuMessage = (updatevalue)=>{
  menuMessage.value = updatevalue
  store.commit("switchPage",{"pageid":updatevalue,"url":''})
}

onMounted(()=>{
  let pageid = localStorage.getItem("lastPage")
  let url = localStorage.getItem("url")
  if(pageid){
    store.commit("switchPage",{"pageid":pageid,"url":url})
  }
})

var p = new Promise((resolve,reject)=>{
  console.log("Promise")
  resolve(1)
}).then((res)=>
{
  console.log("then",res)
  return Promise.reject(2)
}).then((res)=>
{
  console.log("then",res)
  return Promise.resolve(3)
}).catch((err)=>{
  console.log("catch",err)
}).then((res)=>
{
  console.log("then",res)
  return Promise.reject(4)
}).catch((err)=>{
  console.log("catch",err)
})
</script>

<style scoped>
.logout_button{
    display: flex;
  justify-content: flex-end;
  float: right;
}
.common-layout{
    height:100%
}
.el-container {   
    height: 100%;    
  }

  .el-header{/*可以直接使用elementui的标签作为css选择器*/
    background-color: #373d41;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    color: #fff;
    font-size:20px;
  }


  .el-main{
    background-color: #eaedf1;
  }
</style>
