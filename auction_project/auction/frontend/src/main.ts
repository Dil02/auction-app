import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
// import {createRouter,createWebHistory} from 'vue-router'

// const router=createRouter({
//     history:createWebHistory(),
//     routes:[]
// })

createApp(App).use(router).mount('#app')
