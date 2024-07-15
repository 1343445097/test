<template>

    <h1>视频流管理</h1>
    <el-button @click="videoListGet">获取视频流信息</el-button>

    <el-table :data="tableData" border style="width: 100%">
    <el-table-column prop="ori" label="来源" width="100" />
    <el-table-column prop="code" label="视频流" width="100" />
    <el-table-column prop="status" label="状态" />
    <el-table-column prop="clients" label="在线人数" />
    <el-table-column prop="produce_speed" label="入口带宽" />
    <el-table-column prop="video" label="视频信息" />
    <el-table-column prop="audio" label="音频信息" />
    <el-table-column prop="address" label="操作" >
        <template #default="scope">
        <el-button link type="primary" size="small" @click="jumpToVideo(scope.row)">
          预览
        </el-button>
      </template>
        </el-table-column>
  </el-table>
</template>
<!-- 来源	视频流	状态	在线人数	入口带宽	视频信息	音频信息	操作 -->
<script setup>
import { inject,ref,computed,onMounted } from 'vue'
import { useStore } from 'vuex'
const axios = inject('$axios')
const store = useStore()
const videoList = ref([])
const tableData = computed(()=>{
    return videoList.value.map((one)=>{
        return {
            "ori":one.ori,
            "code":one.code,
            "status":"在线",
            "clients":one.clients,
            "produce_speed":one.produce_speed,
            "video":one.video,
            "audio":one.audio,
            "flvUrl":one.flvUrl,
            "hlsUrl":one.hlsUrl
        }
    })
})

//跳转到视频
const jumpToVideo=(row)=>{
    store.commit("switchPage",{pageid:"2-2",url:row.flvUrl})
}

//从后端获取视频列表
const videoListGet =async ()=>{
    await axios.get(store.state.baseUrl+"getStreams")
    .then((res)=>{
        // console.log(res)
        videoList.value = res.data.data
    })
    .catch((err)=>{
        console.log(err,"videoListGet 获取视频列表失败")
    })
}

onMounted(()=>{
    videoListGet();
})

</script>