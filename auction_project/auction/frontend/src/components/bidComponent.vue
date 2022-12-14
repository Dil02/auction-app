<!--
    1.The selected item page should include the description and details not shown in this page.
    2. Planning to replace description with image of file.
-->

<template>

    <div class="itemBox border bg-secondary rounded pt-5 pb-3 mt-5 me-5">

        <h1 class="jumbotron ms-2 me-2 smallerText">
            Bids for {{ item.name }}
        </h1>

        <p id="bidPrice">
            Current Price : £{{ item.price }}
        </p>

        <h3 class="smallerText">Previous bids</h3>
        <ul class="list-unstyled biggerText">
            <li v-for="bid in bids">{{ bid.time }} : Bid of £{{ bid.amount }} placed by {{ bid.bidder.username }}</li>
        </ul>

        <div class="bidInput input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text">£</span>
            </div>
            <input id="newBid" type="number" class="form-control">
        </div>
        <button @click="processBid" v-if="item.sold == false" class="btn btn-sm btn-success me-2">Place Bid</button>

    </div>

</template>
  
<script>
export default {
    props: ["item"],

    data() {
        return {
            bids: [],
            feedback: 0,
        };
    },
    async mounted() {
        this.displayBids();
    },
    methods: {

        //UNFINISHED METHOD
        async processBid() {
            //MAKE SURE BID CAN BE MADE TO THIS ITEM - LIKE WHETHER IT IS AVAILABLE 
            let givenBid = parseFloat(document.getElementById("newBid").value);
            if (givenBid != NaN) {
                givenBid = parseFloat(givenBid.toFixed(2));
                if (givenBid > parseFloat(this.item.price)) {
                    //PERFORM POST AND ADD THIS BID
                    //CALL DISPLAY BIDS
                    //CHANGE FEEDBACK TO 1
                }
            }
            else {
            }
        },
        async displayBids() {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id + "/bids");
            let data = await response.json();
            this.bids = data.bids;
        },
    },
}
</script>
  
<style scoped>
.itemBox {
    border-color: #008148 !important;
    background-color: #212529 !important;
    width: 55em;
    height: auto;
    color: white;
    text-align: center;
    margin: auto;
    margin-bottom: 2em !important;
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

#bidPrice {
    font-size: 1.5em;
}

.bidInput {
    margin: auto;
    width: 9em;
}
</style>