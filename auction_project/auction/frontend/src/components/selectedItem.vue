<!--
    1.The selected item page should include the description and details not shown in this page.
    2. Planning to replace description with image of file.
-->

<template>

    <div class="itemBox border bg-secondary rounded pt-5 pb-3 mt-5 me-5">

        <h1 class="jumbotron ms-2 me-2 smallerText">
            {{ item?.name }}
        </h1>

        <p>
            Sold by : {{ owner?.username }}
        </p>

        <div class="description">
            <p>{{ item?.description }}</p>
        </div>

        <ul class="list-unstyled biggerText">
            <li>Condition : {{ item?.condition }}</li>
            <br>
            <li class="bold">Bidding Starts : {{ item?.start }}</li>
            <li class="bold">Bidding Ends : {{ item?.end }}</li>
        </ul>

        <router-link :to="{ name: 'auction' }" custom v-slot="{ navigate }">
            <button @click="navigate" role="link" class="btn btn-sm btn-success me-2">Back</button>
        </router-link>
    </div>

    <bidComponent :item="item" />

    <questionAnswer :item="item" />


</template>


<script lang="ts">
type Item = {
    name: string;
    username: string;
    description: string;
    condition: string;
    start: string;
    end: string;
    id: string;
};
type Owner = {
    username: string;

};
import bidComponent from './bidComponent.vue';
import questionAnswer from './questionAnswer.vue';

export default {
    components: {
        bidComponent, questionAnswer
    },
    data() {
        return {
            item: null as null | Item,
            owner: null as null | Owner,
        };
    },
    async mounted() {
        this.getSession();
        let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id, { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" });
        let data = await response.json();

        this.item = data.item;
        this.owner = data.item.owner

    },
    methods: {
        async getSession() {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            let data = await response.json();
            if (data.User == "None") {
                window.location.href = "http://127.0.0.1:8000/login/"
            }
            this.owner = data.User

        },
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