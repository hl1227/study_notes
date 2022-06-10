<template>
  <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      router
      active-text-color="#ffd04b"
      :collapse="isCollapse"> <!-- 控制收缩 -->
    <h3 style="color: white;text-align: center;font-weight:700;padding-top: 20px">{{isCollapse?'后台':'XXX后台管理系统'}}</h3>

    <el-menu-item :index="'/'" :key="'/'" >
      <i class="el-icon-s-home"></i>
      <span slot="title">主页</span>
    </el-menu-item>

    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-document"></i>
        <span>数据</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="/data/type" key="/data/type">分类数据</el-menu-item>
        <el-menu-item index="/data/info" key="/data/info">详情数据</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-menu-item index="/user" >
      <i class="el-icon-user"></i>
      <span slot="title">用户</span>
    </el-menu-item>
    <el-menu-item index="4" disabled>
      <i class="el-icon-setting"></i>
      <span slot="title">设置</span>
    </el-menu-item>

  </el-menu>

</template>


<script>
export default {
  data() {
    return {
      a:1
      // isCollapse: false
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  },
  created() {

  },
  computed:{
    isCollapse(){
      return this.$store.state.tab.isCollapse
    }
  }
}
</script>



<style>
* {margin:0;padding:0}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 100%;
}
.el-menu {
    min-height: 100%;
}
</style>