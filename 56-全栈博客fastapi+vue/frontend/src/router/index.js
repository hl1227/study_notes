import VUE from 'vue'
import VueRouter from 'vue-router'
import defaultLayout from '@/layout/default'

VUE.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/home',
        component: defaultLayout,
        children: [
            {
                path: '/home',
                component: () => import('@/views/Main/Home/Home.vue'),
            }
        ],
    },
    {
        path: '/data',
        redirect: '/data/type',
        component: defaultLayout,
        children: [{
            path: 'type',
            component: () => import('@/views/Main/Data/Type'),
        }, {
            path: 'info',
            component: () => import('@/views/Main/Data/Info'),
        }]
    },
    {
        path: '/user',
        redirect: '/user',
        component: defaultLayout,
        children: [{
            path: '/user',
            component: () => import('@/views/Main/User/index'),
        }]
    }
]
const router = new VueRouter({
    mode: 'history',
    routes
})

export default router