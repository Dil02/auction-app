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

function getCookie(name) {
    let cookieValue = "";
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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
            let givenBid = parseFloat(document.getElementById("newBid").value);
            if (givenBid != NaN) {
                givenBid = parseFloat(givenBid.toFixed(2));
            }

            const newBid = JSON.stringify({
                "itemId": this.$route.params.id,
                "amount": givenBid,

            })

            let response = await fetch("http://127.0.0.1:8000/api/bids/", {
                method: 'POST',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie("csrftoken"),
                },
                body: newBid,
            })

            this.$router.push('/')
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