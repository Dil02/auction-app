<template>
    <div class="container">
        <div class="row">
            <div col-sm-12>
                <h1 class="text-center">Profile Page</h1>
            </div>
        </div>
        <div class="row mt-2">
            <div class="col-sm-6">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="nameExample" id="profileUsername"
                        v-model="userDetails.username">
                    <label for="profileUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Clyde" id="profileFirstName"
                        v-model="userDetails.fname">
                    <label for="profileFirstName">First Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Tyler" id="profileSurname"
                        v-model="userDetails.sname">
                    <label for="profileSurname">Surname</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="name@example.com" id="profileEmail"
                        v-model="userDetails.email">
                    <label for="profileEmail">Email Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="01/01/2000" id="profileDOB"
                        v-model="userDetails.dob">
                    <label for="profileDOB">Date of Birth</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="London" id="profileCity"
                        v-model="userDetails.city">
                    <label for="profileCity">City</label>
                </div>
            </div>
            <div class="col-sm-6">
                <img v-bind:src="'http://localhost:8000' + userDetails.picture" height="350" width="350"
                    alt="Press 'View Profile'">

                <form v-bind:action="'http://localhost:8000/api/profile/' + 1" method="POST"
                    enctype="multipart/form-data" class="mt-2">
                    <input type="file" accept="image/*" name="myFile">
                    <input type="submit">
                </form>

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

function getCookie(name) {
    let cookieValue = null;
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

// Adding local state
export default {
    data() {
        return {
            userDetails: [],
        }
    },
    mounted() {
        this.fetchUserDetails();
    },
    methods: {
        async fetchUserDetails() {
            //Performs an Ajax request to fetch a User's details.
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", {
                credentials: "include", mode: "cors", referrerPolicy: "no-referrer",
            }
            );
            let data = await response.json()
            this.userDetails = data.User
            console.log(this.userDetails)
        },
        async updateUserDetails(user_id) {
            //Performs an Ajax PUT request to update a user's profile.
            const requestOptions = {
                method: "PUT",
                headers: { "Content-Type": "application/json", "X-CSRF-Token": getCookie("csrftoken") },
                body: JSON.stringify({
                    data: {
                        username: document.getElementById("profileUsername").value,
                        fname: document.getElementById("profileFirstName").value,
                        sname: document.getElementById("profileSurname").value,
                        dob: new Date(document.getElementById("profileDOB").value).toISOString().split('T')[0],
                        city: document.getElementById("profileCity").value,
                        email: document.getElementById("profileEmail").value,
                    }
                })
            };
            const response = await fetch("http://localhost:8000/api/users/" + user_id + "/", requestOptions, {
                credentials: "same-origin", mode: "cors", referrerPolicy: "no-referrer",
            });
            const data = await response.json();
            this.updatedAt = data.updatedAt;
        },
    }
}

import 'bootstrap/dist/css/bootstrap.css';

</script>
