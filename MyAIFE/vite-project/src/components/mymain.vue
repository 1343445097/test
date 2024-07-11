<template>
  <div>
    <!-- <el-button @click="currentComponent='1'"></el-button>
    <el-button @click="currentComponent='0'"></el-button>
     <myalgorithm v-if="currentComponent=='1'"></myalgorithm>
     <myvideo v-if="currentComponent == '0'"></myvideo> -->
  </div>
  <el-row :gutter="24">
    <el-col :span="xWidth"
      ><div class="grid-content ep-bg-purple" />
      <div class="x_content">
        <div
          id="mychart"
          style="height: 400px; justify-content: space-between"
          ref="chart"
        ></div>
      </div>
    </el-col>
    <el-col :span="xWidth"
      ><div class="grid-content ep-bg-purple" />
      <div id="mychart2" style="height: 400px" ref="chart2"></div>
    </el-col>
    <el-col :span="xWidth"
      ><div class="grid-content ep-bg-purple" />
      <div id="mychart3" style="height: 400px" ref="chart3"></div>
    </el-col>
  </el-row>

  <el-row>
    <el-col :span="xWidth">
      <el-card style="max-width: 480px">
        <template #header>
          <div class="card-header">
            <span>Card name</span>
          </div>
        </template>
        <p v-for="o in 4" :key="o" class="text item">{{ "List item " + o }}</p>
        <template #footer>Footer content</template>
      </el-card>
    </el-col>
    <el-col :span="xWidth">
      <el-card style="max-width: 480px">
        <template #header>
          <div class="card-header">
            <span>Card name</span>
          </div>
        </template>
        <p v-for="o in 4" :key="o" class="text item">{{ "List item " + o }}</p>
        <template #footer>Footer content</template>
      </el-card>
    </el-col>
    <el-col :span="xWidth">
      <el-card style="max-width: 480px">
        <template #header>
          <div class="card-header">
            <span>Card name</span>
          </div>
        </template>
        <p v-for="o in 4" :key="o" class="text item">{{ "List item " + o }}</p>
        <template #footer>Footer content</template>
      </el-card>
    </el-col>
  </el-row>
  控制面板
</template>
<script setup>
import myalgorithm from "./myalgorithm.vue";
import myvideo from "./myvideo.vue";
import * as echarts from "echarts";
import { BarChart, LineChart } from "echarts/charts";
import { inject, onMounted, ref, reactive } from "vue";
import axios from "axios";
import { useStore } from 'vuex'
import { ElNotification } from 'element-plus'
const store = useStore()
const xWidth = ref(8);
const currentComponent = ref("1");

const chartOptions = ref({
  title: { text: "CPU利用率" },
  xAxis: {
    data: [],
  },
  yAxis: {},
  series: [
    {
      type: "line",
      data: [],
    },
  ],
});
const chartOptions2 = ref({
  title: { text: "CPU利用率2" },
  xAxis: {
    data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  },
  yAxis: {},
  series: [
    {
      type: "line",
      data: [23, 24, 18, 25, 27, 28, 25],
    },
  ],
});

let chart = ref();
let chart2 = ref();
let chart3 = ref();
let charts = ref()
const chartResize = () => {
  if (chart.value) {
    if (window.innerWidth < 900) {
      xWidth.value = 24;
    } else {
      xWidth.value = 8;
    }
  }
};
//绘制
const drawChart=()=>{
  const mychart = echarts.init(chart.value);
  const mychart2 = echarts.init(chart2.value);
  const mychart3 = echarts.init(chart3.value);
  mychart.setOption(chartOptions.value);
  mychart2.setOption(chartOptions2.value);
  mychart3.setOption(chartOptions.value);

  window.addEventListener("resize", () => {
    mychart.resize();
  });
  window.addEventListener("resize", () => {
    mychart2.resize();
  });
  window.addEventListener("resize", () => {
    mychart3.resize();
  });
  return [mychart,mychart2,mychart3]
}
//销毁
const disploseChart = ()=>{
  for (const key of charts.value){
    key.dispose()
  }
}
const redrawChart=()=>{
  for (const key of charts.value){
    key.setOption(chartOptions.value);
  }
}
onMounted(() => {
  charts.value = drawChart()
  window.addEventListener("resize", chartResize);
});

//获取时间
const getNowTime=()=>{

var today = new Date();
 
 // 获取年、月、日、时、分、秒
 var year = today.getFullYear();
 var month = today.getMonth() + 1; // 月份是从 0 开始计数的，需要加1
 var day = today.getDate();
 var hours = today.getHours();
 var minutes = today.getMinutes();
 var seconds = today.getSeconds();
 var formattedTime = (hours < 10 ? "0" : "") + hours + ":" + 
                   (minutes < 10 ? "0" : "") + minutes + ":" + 
                   (seconds < 10 ? "0" : "") + seconds;
return formattedTime
}
//更新表
const updateChart=()=>{
  axios.get(store.state.baseUrl+'getIndex')
  .then((res)=>{
      if (res.data.code !== 0){
        chartOptions.value.series[0].data.push(res.data.os_info.os_virtual_mem_used_rate)
        chartOptions.value.xAxis.data.push(getNowTime())
        console.log(chartOptions.value.series[0].data)
        if (chartOptions.value.series[0].data.length>5){
          chartOptions.value.series[0].data.shift()
          chartOptions.value.xAxis.data.shift()
        }
        redrawChart()
        setTimeout(()=>{updateChart()},1000)
      }else{

      }
  }).catch((err)=>{
    ElNotification.error({
          title: "Info",
          message: "获取CPU利用率失败"+err,
          showClose: false,
        });
        
  })
}
onMounted(()=>{
  updateChart()
  // disploseChart()

})
</script>


<style scoped>
.el-row {
  margin-bottom: 3px;
  padding-bottom: 3px;
  display: flex;
  /* align-content: flex-start; */
  flex-wrap: wrap;
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
.el-card{
  margin-right: 20px;
  margin-right: 20px;
}
</style>
  