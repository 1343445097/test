<template>
  <el-table :data="tableData" style="width: 100%">
    
    <el-table-column fixed prop="date" label="序号" width="150" >
      <template #default="scope">
        {{ scope.row.id }}
        </template>
    </el-table-column>
    
    <el-table-column fixed prop="name" label="名称" width="150" />
    <el-table-column prop="interval" label="检测间隔" width="120" />
    <el-table-column prop="sensitivity" label="灵敏度" width="120" />
    <el-table-column prop="overlap_thresh" label="阈值" width="120" />
    <el-table-column prop="remark" label="备注" width="200" />

    </el-table>
</template>

<script setup>
import { getAlgorithm } from '../http/api'
import { onMounted,ref } from 'vue'
const tableData = ref()
onMounted(()=>{
  getAlgorithm().then((res)=>{
    tableData.value = res
  })
})
</script>
  
  <style scoped>
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>
  