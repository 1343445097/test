import { createApp,provide } from 'vue'
//import './style.css'
import App from './App.vue'
import ElementUi from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import router from './router'
import axios from "axios"

const app = createApp(App)
app.use(ElementUi)
app.use(router)
app.provide('$axios',axios)

import Vuex from 'vuex'
import store from './store'
app.use(Vuex)
app.use(store)
app.mount('#app')
