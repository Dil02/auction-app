import { createApp } from 'vue'
// import './style.css'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'

// import {createRouter,createWebHistory} from 'vue-router'

// const router=createRouter({
//     history:createWebHistory(),
//     routes:[]
// })

createApp(App).use(router).mount('#app')
