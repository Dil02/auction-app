<template>
    <div class="container-fluid">
        <div class="row">
            <div col-sm-12>
                <h1 class="text-center">Profile Page</h1>
            </div>
        </div>
        <div class="row mt-2">
            <div class="col-sm-4">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="nameExample" id="profileUsername" v-model="userDetails.username">
                    <label for="profileUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Clyde" id="profileFirstName" v-model="userDetails.fname">
                    <label for="profileFirstName">First Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Tyler" id="profileSurname" v-model="userDetails.sname">
                    <label for="profileSurname">Surname</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="name@example.com" id="profileEmail" v-model="userDetails.email">
                    <label for="profileEmail">Email Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="01/01/2000" id="profileDOB" v-model="userDetails.dob">
                    <label for="profileDOB">Date of Birth</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="London" id="profileCity" v-model="userDetails.city">
                    <label for="profileCity">City</label>
                </div>
            </div>
            <div class="col-sm-8">
                <!-- <img src="..." alt="..." class="img-thumbnail"></img> -->
                <input type="file" accept="image/*" id="pictureUpload">
                <button @click="createImage()">Submit</button>
            </div>
        </div>
        <div class="row">
            <div col-sm-6>
                <button @click="fetchUserDetails(1)">View profile</button>
            </div>
            <div col-sm-6>
                <button @click="updateUserDetails(1)" class="mt-2">Update profile</button>
            </div>
        </div>
    </div>
</template>

<script>

// Adding local state
export default {
  data() {
    return {
      userDetails: [],
    }
  },
  methods: {
    async fetchUserDetails(user_id) {
        //Performs an Ajax request to fetch a User's details.
        let response = await fetch("http://localhost:8000/api/users/" + user_id + "/")
        let data = await response.json()
        this.userDetails = data.user
        console.log(this.userDetails)
    },
    async updateUserDetails(user_id)
    {
      //Performs an Ajax PUT request to update a user's profile.
      const requestOptions = {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ data : {
          username: document.getElementById("profileUsername").value,  
          fname: document.getElementById("profileFirstName").value,
          sname: document.getElementById("profileSurname").value,
          dob: new Date(document.getElementById("profileDOB").value).toISOString().split('T')[0],
          city: document.getElementById("profileCity").value,
          email: document.getElementById("profileEmail").value,}})
      };
      const response = await fetch("http://localhost:8000/api/users/" + user_id + "/", requestOptions);
      const data = await response.json();
      this.updatedAt = data.updatedAt;
      this.fetchUserDetails()
    },
    async createImage()
    {
        const imageInput = document.getElementById("pictureUpload")
        let image = imageInput.files[0]
        console.log(image)

        let formData= new FormData()

        formData.append('picture',image)
        let newImage = fetch("http://localhost:8000/api/users/" + user_id + "/")

    }
  }
}

import 'bootstrap/dist/css/bootstrap.css';

</script>
