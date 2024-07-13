<template>
    <el-row :gutter="20">
      <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="6" :offset="6">
        <div class="grid-content ep-bg-purple" />
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6" :offset="6">
        <div class="grid-content ep-bg-purple" />
      </el-col>
      <el-col :span="6" :offset="6">
        <div class="grid-content ep-bg-purple" />
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content ep-bg-purple" />
      </el-col>
    </el-row>
    vijdeod
    <!-- <videoPlay  v-bind="videoOptions.playerOptions"></videoPlay> -->
    <!-- <vue3videoPlay :src="videoOptions.src" :poster="videoOptions.poster" ></vue3videoPlay> -->
     <video ref="videoElement" controls autoplay>123</video>
  </template>
  
  <script setup>

import { onMounted, reactive,ref } from 'vue'
import   { videoPlay }   from 'vue3-video-play'
import 'vue3-video-play/dist/style.css'
import 'videojs-flash'

import flvjs from 'flv.js';

const videoOptions = reactive({
  // src:"https://media.w3.org/2010/05/sintel/trailer.mp4",
  src:"rtmp://127.0.0.1:1935/live/test3",
  poster:'https://img-blog.csdnimg.cn/img_convert/8273c8dfa2db7b33d90d0584b8382c7f.png',
  playerOptions:{
  width: '800px', //播放器高度
  height: '450px', //播放器高度
  color: "#409eff", //主题色
  muted: false, //静音
  webFullScreen: false,
  speedRate: ["0.75", "1.0", "1.25", "1.5", "2.0"], //播放倍速
  autoPlay: false, //自动播放
  loop: false, //循环播放
  mirror: false, //镜像画面
  ligthOff: false,  //关灯模式
  volume: 0.3, //默认音量大小
  control: true, //是否显示控制器
  title: '', //视频名称
  type: 'rtmp/mp4/flv',
  // src: "http://vjs.zencdn.net/v/oceans.mp4", //视频源
  // src:"rtmp://127.0.0.1:1935/live/test3",
  src:"http://127.0.0.1:80/live/test3.live.flv",
  poster: '', //封面
}
})

let videoElement = ref()
const player = ()=>{
  if (flvjs.isSupported()){
    const flvPlayer = flvjs.createPlayer({
        type: 'flv',
        url: 'http://127.0.0.1:80/live/test3.live.flv'
      });
      flvPlayer.attachMediaElement(videoElement.value);
      flvPlayer.load();
      flvPlayer.play();
  }
}
onMounted(()=>{player()})
</script>
  <style>
  .el-row {
    margin-bottom: 20px;
  }
  .el-row:last-child {
    margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  </style>
  