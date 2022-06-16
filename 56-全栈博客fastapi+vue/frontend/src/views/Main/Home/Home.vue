<template>
  <el-row class="home" :gutter="20">
    <el-col :span="8" style="margin-top: 0px;margin-left:0px">
      <el-card shadow="hover">
        <div class="user">
          <el-avatar :size="60" :src="userIMG"></el-avatar>
          <div class="userinfo">
            <p class="name">{{ nickName }}</p>
            <p class="access">{{ Authority }}</p>
          </div>
        </div>
        <div class="login-info">
          <p>上次登录时间:<span>{{ lastTime }}</span></p>
          <p>上次登录地点:<span>武汉</span></p>
        </div>
      </el-card>
      <el-card style="margin-top: 20px;height: 460px">
        <el-table :data="tableData">
          <el-table-column v-for="(val,key) in tableLabel" :key='key' :prop="key" :label="val"></el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <el-col :span="16" style="margin-top: 0px;margin-left:0px">
      <div class="num">
        <el-card v-for="item in countData" :key="item.name" body-
                 style="display: inline-block;height:80px;width:33.3%;margin-bottom: 5px">
          <i class="icon" :class="item.icon" :style="{background:item.color}"></i>
          <div class="detail" style="display: inline-block">
            <p class="num">¥{{ item.value }}</p>
            <p class="txt">{{ item.name }}</p>
          </div>
        </el-card>
      </div>
      <el-card style="height: 280px;margin-top: 15px">
        <div style="height:280px;width:100%" ref="echarts">
        </div>
      </el-card>
      <div class="graph" style="">
        <el-card style="width:49.5%;height:260px;margin-top:20px;display: inline-block;margin-right:1%">
          <div style="height:240px" ref="pie_1"></div>
        </el-card>
        <el-card style="width:49.5%;height:260px;margin-top:20px;display: inline-block">
          <div style="height:260px;width: 50%;display: inline-block" ref="pie_2"></div>
          <div style="height:260px;width: 50%;display: inline-block" ref="pie_3"></div>
        </el-card>
      </div>

    </el-col>
  </el-row>
</template>
<script>

import {
  index_active_user,
  index_table_data,
  admin_index_line_chart_data,
  admin_index_pie_chart_data,
  admin_index_histogram_data
} from '@/api/data'
import * as echarts from 'echarts'

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      nickName: '',
      Authority: '',
      userIMG: '',
      lastTime: '',
      tableData: [],
      tableLabel: {
        name: '姓名',
        age: '年龄',
        sex: '性别',
        other: '其他'
      },
      countData: [
        {name: '今日支付订单', value: 1234, icon: 'el-icon-success', color: '#2ec7c9'},
        {name: '今日收藏订单', value: 2234, icon: 'el-icon-success', color: '#2ec7c9'},
        {name: '今日未支付订单', value: 3234, icon: 'el-icon-success', color: '#2ec7c9'},
        {name: '本月支付订单', value: 4234, icon: 'el-icon-success', color: '#2ec7c9'},
        {name: '本月收藏订单', value: 5234, icon: 'el-icon-success', color: '#2ec7c9'},
        {name: '本月未支付订单', value: 6234, icon: 'el-icon-success', color: '#2ec7c9'},
      ]
    }
  },
  mounted() {
    index_active_user().then(response => {
      let data = response.data
      if (data.code === 200) {
        this.nickName = data.data.nickname
        this.Authority = data.data.authority
        this.userIMG = data.data.headshot_src
        this.lastTime = data.data.last_time
      }
    });
    index_table_data().then(response => {
      let data = response.data
      if (data.code === 200) {
        this.tableData = data.data.list
      }
    });
    admin_index_line_chart_data().then(response => {
      let data = response.data
      if (data.code === 200) {
        const xData = data.data.xdata
        const keyArray = Object.keys(data.data.ydata[0])
        const series = []
        keyArray.forEach(key => {
          series.push({
            name: key,
            data: data.data.ydata.map(item => item[key]),
            type: 'bar',//line为条形图
            emphasis: {label: {show: true}}
          })
        })
        const option = {
          title: {text: 'bar为柱状图'},
          xAxis: {data: xData},
          yAxis: {},
          legend: {data: keyArray},
          series
        }
        const E = echarts.init(this.$refs.echarts)
        E.setOption(option)
      }
    });
    admin_index_pie_chart_data().then(response => {
      let data = response.data
      if (data.code === 200) {

        const option = {
          title: {text: 'pie为饼状图'},
          tooltip: {trigger: 'item'},
          series: [
            {
              type: 'pie',
              data: data.data.pie1,
              radius: ['30%', '70%'],

              // itemStyle: {
              //   borderRadius: 10,
              //   borderColor: '#fff',
              //   borderWidth: 2
              // },
            }]
        }
        const p1 = echarts.init(this.$refs.pie_1)
        p1.setOption(option)
      }
    });
    admin_index_histogram_data().then(response => {
      let data = response.data
      if (data.code === 200) {
        const l1 = []
        l1.push(data.data.pie2[0])
        const option = {
          tooltip: {formatter: '888'},
          series: [
            {
              name: 'Pressure',
              type: 'gauge',
              detail: {formatter: '{value}%'},
              data: l1
            }]
        }
        const p2 = echarts.init(this.$refs.pie_2)
        p2.setOption(option)
//////////////////////////////////////////////////////////////
        const l3 = []
        l3.push(data.data.pie2[1])
        const option3 = {
          tooltip: {formatter: '888'},
          series: [
            {
              name: 'Pressure3',
              type: 'gauge',
              detail: {formatter: '{value}%'},
              data: l3
            }
          ]
        }
        const p3 = echarts.init(this.$refs.pie_3)
        p3.setOption(option3);
      }
    });
  }
}
</script>

<style lang="less" scoped>
//.icon{
//  height: 100%;
//}

</style>
