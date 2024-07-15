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
    <!-- <videoPlay  :src="videoOptions.src" v-bind="videoOptions.playerOptions"></videoPlay> -->
    <!-- <videoPlay :src="videoOptions.src" :poster="videoOptions.poster" ></videoPlay> -->
     <div style="border-color:blue;border-width:1px;width: 800px;height: 600px">
      <video style="width: 600px;height: 400px;" ref="videoElement" controls autoplay>123</video>
     </div>
  </template>
  
  <script setup>
import { useStore } from 'vuex'
const store = useStore()
import { onMounted, reactive,ref } from 'vue'
import flvjs from 'flv.js';
//另一种播放器
// import   { videoPlay }   from 'vue3-video-play'
// import 'vue3-video-play/dist/style.css'
// import 'videojs-flash'

// const videoOptions = reactive({
//   src:"https://media.w3.org/2010/05/sintel/trailer.mp4",
//   // src:"../static/test.mp4",
//   // src:"rtmp://127.0.0.1:1935/live/test3",
//   poster:'https://img-blog.csdnimg.cn/img_convert/8273c8dfa2db7b33d90d0584b8382c7f.png',
//   playerOptions:{
//   width: '800px', //播放器高度
//   height: '450px', //播放器高度
//   color: "#409eff", //主题色
//   muted: false, //静音
//   webFullScreen: false,
//   speedRate: ["0.75", "1.0", "1.25", "1.5", "2.0"], //播放倍速
//   autoPlay: false, //自动播放
//   loop: false, //循环播放
//   mirror: false, //镜像画面
//   ligthOff: false,  //关灯模式
//   volume: 0.3, //默认音量大小
//   control: true, //是否显示控制器
//   title: '', //视频名称
//   type: 'mp4',
//   // src: "http://vjs.zencdn.net/v/oceans.mp4", //视频源
//   src:"https://media.w3.org/2010/05/sintel/trailer.mp4",
//   // src:"http://127.0.0.1:80/live/test3.live.flv",
//   poster: '', //封面
// }
// })

//flv.js播放器
let videoElement = ref()
const player = ()=>{
  if (flvjs.isSupported()){ 
    const flvPlayer = flvjs.createPlayer({
        type: 'flv',
        // url: 'http://127.0.0.1:80/live/test3.live.flv'
        url: store.state.myvideo_.url
        // type:"rtmp",
        // url:"rtmp://127.0.0.1:1935/live/test3"
        // type:'mp4',
        // url:'https://media.w3.org/2010/05/sintel/trailer.mp4',

      });
      // flvPlayer.scaleToContainer({width:600,height: 400})
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
  