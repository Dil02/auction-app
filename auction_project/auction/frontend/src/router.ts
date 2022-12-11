import {createRouter,createWebHistory} from 'vue-router'


const routes=[  
    {path:'/test',name:"home",component:() => import('./components/HelloWorld.vue')},
    {path:'/item',name:"item",component:() => import('./components/AddItem.vue')},
    {path:'/helloWorld',name:"home",component:() => import('./components/HelloWorld.vue')},
    {path: '/profile', name:"profile",component:() => import('./components/Profile.vue')},


]

const router=createRouter({
    routes,
    history:createWebHistory()
    
})

export default router