import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    { path: '/', name: "auction", component: () => import('./components/auction.vue') },
    { path: '/item', name: "item", component: () => import('./components/AddItem.vue') },
    { path: '/profile', name: "profile", component: () => import('./components/Profile.vue') },


]

const router = createRouter({
    routes,
    history: createWebHistory()

})

export default router