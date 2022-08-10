<template>
  <header >
    <div class="l-content">
      <el-button @click="handleMenu" plain  icon="el-icon-s-grid" size="mini"></el-button>
      <el-breadcrumb separator=">">
        <el-breadcrumb-item v-for="item in tags" :key="item.path" :to={path:item.path} >
          <span style="color: white">{{item.label}}</span>
        </el-breadcrumb-item>

      </el-breadcrumb>
    </div>
    <div class="r-conent" >
      <el-dropdown>
      <span class="el-dropdown-link">
          <p style="color: white"><el-avatar size="medium" :src="userIMG" ></el-avatar >username<i class="el-icon-arrow-down el-icon--right"></i></p>
      </span>
        <el-dropdown-menu slot="dropdown" style="background-color: #336666;">
          <el-dropdown-item style="color: white" icon="el-icon-user-solid">个人中心</el-dropdown-item>
          <el-dropdown-item style="color: white" icon="el-icon-remove">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </header>
</template>

<script>
import {mapState} from 'vuex'
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
  },
  computed:{
    ...mapState({
      tags:state=>state.tab.tabsList
    })
  }
}
</script>

<style lang="less" scoped>
header {

  display: flex;
  background-color: #336666;
  //#333333
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