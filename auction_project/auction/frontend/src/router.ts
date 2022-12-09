import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    { path: '/test', name: "home", component: () => import('./components/HelloWorld.vue') },
    { path: '/homePage', name: "homePage", component: () => import('./components/HomePage.vue') },

]

const router = createRouter({
    routes,
    history: createWebHistory()

})

export default router