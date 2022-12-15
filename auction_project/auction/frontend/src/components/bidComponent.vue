<!--
    1.The selected item page should include the description and details not shown in this page.
    2. Planning to replace description with image of file.
-->

<template>

    <div class="itemBox border bg-secondary rounded pt-5 pb-3 mt-5 me-5">

        <h1 class="jumbotron ms-2 me-2 smallerText">
            Bids for {{ item?.name }}
        </h1>

        <p id="bidPrice">
            Current Price : £{{ latestPrice }}
        </p>

        <h3 class="smallerText">Previous bids</h3>
        <ul class="list-unstyled biggerText">
            <li v-for="bid in bids" :key="bid.id">{{ bid.time }} : Bid of £{{ bid.amount }} placed by {{
                    bid.bidder.username
            }}</li>
        </ul>

        <div v-show="provideInput" class="bidInput input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text">£</span>
            </div>
            <input id="newBid" type="number" class="form-control">
        </div>
        <button @click="processBid" v-show="provideInput" class="btn btn-sm btn-success me-2">Place Bid</button>
        <p class="errorMsg bold" v-if="invalidInput">Please check your input. Make sure your bid is higher than the
            price.
        </p>
        <p class="successMsg bold" v-if="validInput">Your bid has been successfully added. </p>

    </div>

</template>
  
<script lang="ts">
function getCookie(name: String) {
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

type User = {
    username: string;
    fname: string;
    sname: string;
    dob: string;
    city: string;
    email: string;
    id: string;
};

type Bid = {
    bidder: User;
    time: string;
    amount: String;
    id: string;
};

export default {
    props: ["item"],
    data() {
        return {
            bids: [] as Bid[],
            provideInput: true,
            invalidInput: false,
            validInput: false,
            latestPrice: 0,
        };
    },
    async mounted() :Promise<void> {
        this.available()
        this.displayBids();
    },
    methods: {

        async processBid():Promise<void> {
            let givenElement = document.getElementById("newBid") as HTMLInputElement
            let givenBid;
            if (givenElement == null) {
                return;
            }
            else {
                givenBid = parseFloat(givenElement.value)
            }

            if (!Number.isNaN(givenBid)) {
                givenBid = parseFloat(givenBid.toFixed(2));

                let currentPrice = parseFloat(this.item.price);
                if (givenBid <= currentPrice) {
                    this.invalidInput = true;
                    this.validInput = false;
                    return
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

                this.validInput = true;
                this.invalidInput = false;
                this.displayBids();
                this.latestPrice = givenBid;
            }
            else {
                this.invalidInput = true;
                this.validInput = false;
            }


        },
        async displayBids() :Promise<void>{
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id + "/bids");
            let data = await response.json();
            this.bids = data.bids;
        },

        async available():Promise<void> {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id);
            let data = await response.json();
            let record = data.item;
            let start = record.start
            let end = record.end
            let sold = record.sold
            let owner = record.owner
            this.latestPrice = record.price

            if (sold == true) {
                this.provideInput = false;
                return;
            }

            const startTimestamp = new Date(Date.parse(start));
            const endTimestamp = new Date(Date.parse(end));
            let current = new Date();

            if (endTimestamp < startTimestamp || endTimestamp < current) {
                this.provideInput = false;
                return;
            }

            let ownerComparison = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" });
            let ownerData = await ownerComparison.json()

            if (ownerData.User.id == owner.id) {
                this.provideInput = false;
                return;
            }
            return;
        }
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

.errorMsg {
    color: red;
}

.successMsg {
    color: green;
}

.bidInput {
    margin: auto;
    width: 9em;
}
</style>