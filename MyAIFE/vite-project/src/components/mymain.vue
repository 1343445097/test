<template>
  <div>
    <!-- <el-button @click="currentComponent='1'"></el-button>
    <el-button @click="currentComponent='0'"></el-button>
     <myalgorithm v-if="currentComponent=='1'"></myalgorithm>
     <myvideo v-if="currentComponent == '0'"></myvideo> -->
  </div>
  控制面板
</template>
<script setup>
import myalgorithm from './myalgorithm.vue'
import myvideo from './myvideo.vue'
import {ref} from 'vue'

const currentComponent = ref('1')

</script>
  <style scoped>
.el-row {
  margin-bottom: 20px;
  padding-bottom: 30px;
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
  