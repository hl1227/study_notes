<template>
 <el-container style="height: 100%">
  <el-aside width="auto">
    <common-aside ></common-aside>
  </el-aside>
  <el-container>
    <el-header style="padding: 0">
      <common-header></common-header>
    </el-header>

    <el-main>
      <router-view/>
    </el-main>
    <el-footer>Footeraaaaaaaaaaaaaaa</el-footer>
  </el-container>
  </el-container>
</template>

<script>
import CommonAside from "@/components/CommonAside.vue";
import CommonHeader from "@/components/CommonHeader";
export default {
  name: "default",
  components:{CommonAside,CommonHeader}
}
</script>

<style scoped>

</style>