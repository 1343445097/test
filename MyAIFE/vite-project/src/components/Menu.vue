<template>
  <!-- <h5 class="mb-2">Custom colors</h5> -->
  <el-aside width="200px">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
      <el-radio-button :value="false">expand</el-radio-button>
      <el-radio-button :value="true">collapse</el-radio-button>
    </el-radio-group>
    <el-menu
      active-text-color="#ffd04b"
      background-color="#545c64"
      class="el-menu-vertical-demo"
      default-active="2"
      text-color="#fff"
      :collapse="isCollapse"
      @open="handleOpen"
      @close="handleClose"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><location /></el-icon>
          <span>主页</span>
        </template>
        <el-menu-item  @click="switchPage" index="1-1">控制面板</el-menu-item>

      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>
          <el-icon><icon-menu /></el-icon>
          <span>视频流</span>
        </template>
        <el-menu-item @click="switchPage" index="2-1">视频流管理</el-menu-item>
        <el-menu-item @click="switchPage" index="2-2" >预览</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3" >
        <template #title>
          <el-icon><document  /></el-icon>
          <span>算法</span>
        </template>
        <el-menu-item @click="switchPage" index="3-1">算法管理</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="4">
        <template #title>
          <el-icon><setting  /></el-icon>
          <span>布控</span>
        </template>
        <el-menu-item @click="switchPage" index="4-1">布控管理</el-menu-item>
        <el-menu-item @click="switchPage" index="4-2">添加布控</el-menu-item>
        <el-menu-item @click="switchPage" index="4-3">编辑布控</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </el-aside>
</template>

<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from "@element-plus/icons-vue";
import { ref } from "vue";
const isCollapse = ref(false);
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
  
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
//父方法
let emit = defineEmits(['menu-event'])
const menuHandle=(chosePage)=>{
  emit('menu-event',chosePage)
}
//切换页面
const switchPage=(form1)=>{
  //console.log("switch",form1,form1.index)
  menuHandle(form1.index)
}
</script>

<style scoped>
  .el-aside {
        background-color: rgb(61, 61, 61);
        color: #333;
        /* text-align: center; */
        /* line-height: 200px; */
    }
</style>