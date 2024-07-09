import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import ElementUi from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import router from './router'
import Vuex from 'vuex'

const app = createApp(App)
app.use(ElementUi)
app.use(router)
app.use(Vuex)
app.mount('#app')
