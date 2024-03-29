import { createRouter, createWebHistory } from 'vue-router'


const routes = [

    { path: '/', name: "auction", component: () => import('./components/auction.vue') },
    { path: '/item', name: "item", component: () => import('./components/AddItem.vue') },
    { path: '/profile', name: "profile", component: () => import('./components/Profile.vue') },
    { path: '/item/:id', name: "selectedItem", component: () => import('./components/selectedItem.vue') },
    { path: '/logout', name: "logout", component: () => import('./components/logout.vue') },
    { path: '/yo', name: "test", component: () => import('./components/questionAnswer.vue') },//Test


]

const router = createRouter({
    routes,
    history: createWebHistory()

})

export default router