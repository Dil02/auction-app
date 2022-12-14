<template>
    <div>
        <form class="w-75 mx-auto mt-2 pt-2 d-flex flex-column justify-content-center p-2 bg-dark text-light rounded"
            id="form1" @submit.prevent="saveNewObject()">
            <div class="form-input ml-auto">
                <h3><label class="form-label" for="image">Choose a image</label></h3>
                <input type="file" accept="image/*" @change="storeImage" class="form-control-file">
                <img class="img-fluid rounded mx-auto" height=400 v-if="picture" :src="picture" />
            </div>
            <div class="form-input">
                <h3><label class="form-label" for="name">Name of Product</label></h3>
                <input v-model="name" type="text" class="form-control" placeholder="Enter name">
            </div>
            <div class="form-input mb-2">
                <h3><label for="Description">Description</label></h3>
                <textarea v-model="desc" class="form-control" id="Desc" rows="4" required></textarea>
            </div>
            <div class="form-input">
                <h3><label class="form-label" for="price">Set Price</label></h3>
                <input v-model="price" type="text" class="form-control" placeholder="Enter value">
            </div>
            <div class="form-group">
                <h3><label for="options">Select Condition</label></h3>
                <select v-model="condition" class="form-control" id="options" required>
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
                    <input v-model=start id="startDate" class="form-control" type="date" required />
                </div>

                <div class="d-inline">
                    <h3><label for="endDate">End Date</label></h3>
                    <div style="clear: both;"></div>
                    <input v-model=end id="endDate" class="form-control" type="date" required />
                </div>

            </div>

            <button type="submit" class="btn btn-primary mt-4 pt-2 w-50 mb-3" id="b">Submit</button>

        </form>
    </div>
</template>

<script lang="ts">

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
    methods: {
        async saveNewObject() {
            const item = JSON.stringify({
                name: this.name,
                condition: this.condition,
                price: this.price,
                description: this.desc,
                start: this.start,
                end: this.end,
                sold: false,
                picture: this.picture,
            })
            console.log(item)
            let response = await fetch("http://localhost:8000/api/items/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: item,
            })

        },

        async storeImage(e: any) {
            const file = e.target.files[0];
            this.prev = URL.createObjectURL(file);  //creates a blob image (to preview image)
            var reader = new FileReader();
            this.picture = await new Response(this.prev).text()  // changes blob to string (to store)

        }
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