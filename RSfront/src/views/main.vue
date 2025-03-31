<template>
    <div class="mainbody">
      <h1 class="headtitle">遥感解译平台首页</h1>
      <!-- <h2 class="">{{ demoStore.helloPinia }}</h2> -->
      <!-- <el-button type="primary">此处使用Element-Plus</el-button> -->
    </div>
</template>

<script setup lang="ts">
import { mainStore } from '../store';
import { storeToRefs } from 'pinia';  /* 引入storeToRefs */
import axios from 'axios';

const demoStore = mainStore();  /* 创建store实例 */

const adduser=()=>{
  let formData=new FormData();
  formData.append('username','12345');
  formData.append('password','54321');
  let url='http://127.0.0.1:5000/adduser'  //后端接口地址
  let method='post'
  axios({
    method,
    url,
    data:formData,
  }).then(res=>{
    alert(res.data)
  });
}
adduser();

</script>
  
<style scoped>
    .mainbody {
      height: 6em;
      padding: 1.5em;
      will-change: filter;
      transition: filter 300ms;
    }
    .headtitle {
      filter: drop-shadow(0 0 2em #646cffaa);
    }
</style>