<template>
    <div>
        <form
            class="w-75 mx-auto mt-2 pt-2 d-flex flex-column justify-content-center align-items-center  p-2 bg-dark text-light "
            id="form1" @submit="saveNewObject()">
            <div class="form-input">
                <label class="form-label" for="image">Choose a image</label>
                <input accept="image/jpeg, image/png" type="file" class="form-control" @change="uploadImages" id="image"
                    required />
            </div>
            <div class="form-input">
                <label class="form-label" for="name">Name of Product</label>
                <input v-model="name" type="text" class="form-control" placeholder="Enter name">
            </div>
            <div class="form-group mb-2">
                <label for="Description">Description</label>
                <textarea v-model="desc" class="form-control" id="Desc" rows="4" required></textarea>
            </div>
            <div class="form-input">
                <label class="form-label" for="price">Set Price</label>
                <input v-model="price" type="text" class="form-control" placeholder="Enter name">
            </div>
            <div class="form-group">
                <label for="options">Select Condition</label>
                <select v-model="type" class="form-control" id="options" required>
                    <option value="NEW">NEW</option>
                    <option value="UE">USED - EXCELLENT</option>
                    <option value="UG">USED - GOOD</option>
                    <option value="UA">USED - ACCEPTABLE</option>
                </select>
            </div>
            <div class="form-group mb-2 inline">

                <div class="d-inline">
                    <label for="startDate">Start Date</label>
                    <div style="clear: both;"></div>
                    <input v-model=start id="startDate" class="form-control" type="date" required />
                </div>

                <div class="d-inline">
                    <label for="endDate">End Date</label>
                    <div style="clear: both;"></div>
                    <input v-model=end id="endDate" class="form-control" type="date" required />
                </div>

            </div>

            <button type="submit" class="btn btn-primary mt-4 pt-2 w-50 mb-3">Submit</button>

        </form>
    </div>
</template>

<script lang="ts">

export default {

    data() {
        return {
            type: "",
            name: "",
            picture: null,
            price: null,
            start: null,
            end: null,
            desc: "",


        }
    },
    methods: {
        async saveNewObject() {
            const item = JSON.stringify({
                name:this.name,
                Type: this.type,
                price: this.price,
                description: this.desc,
                start: this.start,
                end: this.end,
                picture:this.picture,
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
        uploadImages(e: any) {
            this.picture = e.target.files[0];
        }
    }
}  
</script>

<style scoped>

</style>