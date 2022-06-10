<template>
  <header >
    <div class="l-content">
      <el-button @click="handleMenu" plain  icon="el-icon-s-grid" size="mini"></el-button>
      <h3>首页</h3>
    </div>
    <div class="r-conent" >
      <el-dropdown>
      <span class="el-dropdown-link">
          <el-avatar size="medium" :src="userIMG" ></el-avatar>username<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item icon="el-icon-user-solid">个人中心</el-dropdown-item>
          <el-dropdown-item icon="el-icon-remove">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </header>
</template>

<script>
export default {
  name: "CommonHeader",
  data(){
    return{
      userIMG:'https://t7.baidu.com/it/u=2168645659,3174029352&fm=193&f=GIF'
    }
  },
  methods:{
    handleMenu(){
      this.$store.commit('collapseMenu')
    }
  }
}
</script>

<style lang="less" scoped>
header {
  display: flex;
  background-color: #333333;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 20px;
  .l-content {
    display: flex;
    align-items: center;
    .el-button{
      margin-right: 20px;
    }
  };
  .r-conent{

  }
}
</style>