<template>
  <el-row class="home" :gutter="20">
    <el-col :span="8" style="margin-top: 20px;margin-left:10px">
      <el-card shadow="hover">
        <div class="user">
          <el-avatar size="" :src="userIMG" ></el-avatar>
          <div class="userinfo">
            <p class="name">username</p>
            <p class="access">权限</p>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>
<script>

export default {
  name:'Home',
  components:{
  },
  data(){
    return{
      userIMG:'https://t7.baidu.com/it/u=2168645659,3174029352&fm=193&f=GIF'
    }
  },
}
</script>

<style lang="less" scoped>


</style>
