<template>
<!-- #545c64 -->
  <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      router
      active-text-color="yellow"
      :collapse="isCollapse"> <!-- 控制收缩 -->
    <h3 style="color: white;text-align: center;font-weight:700;padding-top: 20px">{{ isCollapse ? '后台' : 'XXX后台管理系统' }}</h3>

    <template v-for="(t, i) in pathDate">
      <div v-if="t.children" :key="i">
        <el-submenu :index="t.path">
          <template slot="title">
            <i class="el-icon-document"></i>
            <span>{{ t.label }}</span>
          </template>
          <el-menu-item-group v-for="child in t.children" :key="child.path">
            <el-menu-item @click="clickMenu(child)" :index="child.path" style="width: 50%">
              <i :class="child.icon"></i>
              {{ child.label }}
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </div>

      <el-menu-item v-else @click="clickMenu(t)" :index="t.path" :key="i">
        <i :class="t.icon"></i>
        <span slot="title">{{ t.label }}</span>
      </el-menu-item>
    </template>

  </el-menu>

</template>


<script>
export default {
  data() {
    return {
      pathDate: [
        {name: 'home', path: '/home', icon: 'el-icon-s-home', label: '首页'},
        {
          name: 'date', path: '/date', icon: 'el-icon-document', label: '数据',
          children: [
            {name: 'cateDate', path: '/data/type', label: '分类数据', icon: 'el-icon-document'},
            {name: 'infoDate', path: '/data/info', label: '详情数据', icon: 'el-icon-document'}]
        },
        {name: 'user', path: '/user', icon: 'el-icon-user', label: '用户'},
        {name: 'setting', path: '/setting', icon: 'el-icon-setting', label: '设置'},
      ],

    }
  },
  methods: {
    handleOpen(key, keyPath) {
      key
      keyPath
    },
    handleClose(key, keyPath) {
      key
      keyPath
    },
    clickMenu(item) {
      // this.$router.push({
      //   path:item.path
      // })
      this.$store.commit('selectMenu', item)
    }
  },
  created() {

  },
  computed: {
    isCollapse() {
      return this.$store.state.tab.isCollapse
    },

  }
}
</script>


<style>
* {
  margin: 0;
  padding: 0
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 210px;
  min-height: 100%;
}

.el-menu {
  min-height: 100%;
}
</style>