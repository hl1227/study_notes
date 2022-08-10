export default {
    state: {
        isCollapse: false, //侧边栏初始数据
        tabsList: [//面包屑
            {path: '/home', name: 'home', label: '首页', icon: 'home'}
        ],
        currentMenu: null
    },
    mutations: {
        //侧边栏开关函数
        collapseMenu(state) {
            state.isCollapse = !state.isCollapse
        },
        selectMenu(state, val) {
            if (val.name !== 'home') {
                state.currentMenu = val
                const result = state.tabsList.findIndex(item => item.name === val.name)
                if (result === -1) {
                    state.tabsList.push(val)
                }
            }else {
                    state.currentMenu = null
            }
        }
    }
}
