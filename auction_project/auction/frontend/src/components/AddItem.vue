<template>
    <div>
        <form class="w-75 mx-auto mt-2 pt-2 d-flex flex-column justify-content-center p-2 bg-dark text-light rounded"
            id="form1" @submit.prevent="saveNewObject()" enctype="multipart/form-data">
            <div class="form-input ml-auto">
                <h3><label class="form-label" for="image">Choose a image</label></h3>
                <input type="file" accept="image/*" name="myFile" id="itemImage">
            </div>

            <div class="form-input">
                <h3><label class="form-label" for="name">Name of Product</label></h3>
                <input v-model="name" type="text" class="form-control" placeholder="Enter name" name="name" id="itemName">
            </div>
            <div class="form-input mb-2">
                <h3><label for="Description">Description</label></h3>
                <textarea v-model="desc" class="form-control" id="itemDesc" rows="4" required name="desc"></textarea>
            </div>
            <div class="form-input">
                <h3><label class="form-label" for="price">Set Price</label></h3>
                <input v-model="price" type="text" class="form-control" placeholder="Enter value" name="value" id="itemValue">
            </div>
            <div class="form-group">
                <h3><label for="options">Select Condition</label></h3>
                <select v-model="condition" class="form-control" id="itemCondition" required name="condition">
                    <option value="NEW">NEW</option>
                    <option value="UE">USED - EXCELLENT</option>
                    <option value="UG">USED - GOOD</option>
                    <option value="UA">USED - ACCEPTABLE</option>
                </select>
            </div>
            <div class="form-group mb-2 inline">

                <div class="d-inline">
                    <h3><label for="startDate">Start Date</label></h3>
                    <div style="clear: both;"></div>
                    <input v-model=start id="itemStartDate" class="form-control" type="date" required name="startDate"/>
                </div>

                <div class="d-inline">
                    <h3><label for="endDate">End Date</label></h3>
                    <div style="clear: both;"></div>
                    <input v-model=end id="itemEndDate" class="form-control" type="date" required name="endDate" />
                </div>

            </div>

            <button type="submit" class="btn btn-primary mt-4 pt-2 w-50 mb-3" id="b">Submit</button>

        </form>
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

    data() {
        return {
            prev: "",
            condition: "",
            name: "",
            picture: '',
            price: null,
            start: null,
            end: null,
            desc: "",


        }
    },
    async mounted() {
        this.getSession();
    },

    methods: {
        async saveNewObject() {
            // const item = JSON.stringify({
            //     name: this.name,
            //     condition: this.condition,
            //     price: this.price,
            //     description: this.desc,
            //     start: this.start,
            //     end: this.end,
            //     sold: false,
            //     picture: this.picture,
            // })

            const formData = new FormData()
            let fileField = document.querySelector("#itemImage")
            formData.append('myFile',fileField.files[0])
            formData.append('name',document.querySelector("#itemName").value)
            formData.append('description',document.querySelector("#itemDesc").value)
            formData.append('price',document.querySelector("#itemValue").value)
            formData.append('condition',document.querySelector("#itemCondition").value)
            formData.append('startDate',document.querySelector("#itemStartDate").value)
            formData.append('endDate',document.querySelector("#itemEndDate").value)
            
            let response = await fetch("http://127.0.0.1:8000/api/items/", {
                method: 'POST',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    // 'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie("csrftoken"),
                },
                body: formData,
            })

            this.$router.push('/')

        },

        // async storeImage(e) {
        //     const file = e.target.files[0];
        //     this.prev = URL.createObjectURL(file);  //creates a blob image (to preview image)
        //     var reader = new FileReader();
        //     this.picture = await new Response(this.prev).text()  // changes blob to string (to store)

        // },

        async getSession() {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            let data = await response.json();
            if (data.User == "None") {
                window.location.href = "http://127.0.0.1:8000/login/"
            }
        },
    }
}  
</script>

<style scoped>
#b {
    margin: auto auto;
}

img {
    max-height: 300px;
    max-width: 300px;
    height: auto;
    width: auto;
}
</style>