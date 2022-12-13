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
            Sold by : {{ item.owner.username }}
        </p>

        <ul class="list-unstyled biggerText">
            <li>Current Price : £{{ item.price }}</li>
            <li>Condition : {{ item.condition }}</li>
        </ul>

        <button class="btn btn-sm btn-success me-2">View</button>
    </div>

</template>
  
<script>
export default {
    props: ["item"],
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
    width: 25em;
    height: auto;
    color: white;
    text-align: center;
}

.fixedSize {
    border: 1px solid blue;
    overflow-y: auto;
    margin-left: 0.2em;
    margin-right: 0.2em;
    height: 6em;
    font-size: 0.8em;
}
</style>