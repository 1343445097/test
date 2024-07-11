import { createApp } from 'vue'
//import './style.css'
import App from './App.vue'
import ElementUi from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import router from './router'


const app = createApp(App)
app.use(ElementUi)
app.use(router)

import Vuex from 'vuex'
import store from './store'
app.use(Vuex)
app.use(store)
app.mount('#app')
