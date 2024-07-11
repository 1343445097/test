import { createRouter,createWebHashHistory } from 'vue-router'

import Login from './components/login.vue'
import HelloWorld from './components/HelloWorld.vue'
import Main from './components/Main.vue'

const routes = [
    {path:'/',
     name:'Home',
     component:Main
    },
    {path:'/login',
    name:'Login',
    component:Login
       },
]

const router = createRouter({
    history:createWebHashHistory(),
    routes
})

export default router