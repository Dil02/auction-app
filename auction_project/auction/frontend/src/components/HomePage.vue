
<template>
    <div class="mainContainer">
        <ItemComponent v-for="item in items" :item="item" />
    </div>

</template>
  
  
<script>
import ItemComponent from './ItemComponent.vue';

export default {
    components: {
        ItemComponent,
    },

    data() {
        return {
            items: [],
        };
    },
    async mounted() {
        let response = await fetch("http://127.0.0.1:8000/api/items/");
        let data = await response.json();
        this.items = data.items;

    },

    methods: {
        async fetchItems() {
            let response = await fetch("http://127.0.0.1:8000/api/items/");
            let data = await response.json();
            this.items = data.items;
        },
    },

}

</script>
  
<style scoped>
.mainContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>