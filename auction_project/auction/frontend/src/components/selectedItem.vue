<!--
    1.The selected item page should include the description and details not shown in this page.
    2. Planning to replace description with image of file.
-->

<template>

    <div class="itemBox border bg-secondary rounded pt-5 pb-3 mt-5 me-5">

        <h1 class="jumbotron ms-2 me-2 smallerText">
            {{ item.name }}
        </h1>

        <p>
            Sold by : {{ owner.username }}
        </p>

        <div class="description">
            <p>{{ item.description }}</p>
        </div>

        <ul class="list-unstyled biggerText">
            <li>Condition : {{ item.condition }}</li>
            <br>
            <li class="bold">Bidding Starts : {{ item.start }}</li>
            <li class="bold">Bidding Ends : {{ item.end }}</li>
        </ul>

        <button class="btn btn-sm btn-success me-2">Back</button>
    </div>

    <bidComponent :item="item" />

</template>


<script>
import bidComponent from './bidComponent.vue';

export default {
    components: {
        bidComponent,
    },
    data() {
        return {
            item: [],
            owner: [],
        };
    },
    async mounted() {
        let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id);
        let data = await response.json();

        this.item = data.item;
        this.owner = data.item.owner

    },
    methods: {

    }
}
</script>
  
<style scoped>
.biggerText {
    font-size: 1.3em;
}

.smallerText {
    font-size: 2em;
}

.itemBox {
    border-color: #008148 !important;
    background-color: #212529 !important;
    width: 55em;
    height: auto;
    color: white;
    text-align: center;
    margin: auto;
    margin-right: auto !important;
}

.description {
    font-size: 1em !important;
    margin-left: 0.2em;
    margin-right: 0.2em;
}

.bold {
    font-weight: bolder;
}
</style>