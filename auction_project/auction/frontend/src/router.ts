import {createRouter,createWebHistory} from 'vue-router'


const routes=[  
    {path:'/test',name:"home",component:() => import('./components/HelloWorld.vue')},


]

const router=createRouter({
    routes,
    history:createWebHistory()
    
})

export default router