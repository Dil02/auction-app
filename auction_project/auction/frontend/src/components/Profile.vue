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
                        v-model="userDetails?.username">
                    <label for="profileUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Clyde" id="profileFirstName"
                        v-model="userDetails?.fname">
                    <label for="profileFirstName">First Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Tyler" id="profileSurname"
                        v-model="userDetails?.sname">
                    <label for="profileSurname">Surname</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="name@example.com" id="profileEmail"
                        v-model="userDetails?.email">
                    <label for="profileEmail">Email Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="01/01/2000" id="profileDOB"
                        v-model="userDetails?.dob">
                    <label for="profileDOB">Date of Birth</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="London" id="profileCity"
                        v-model="userDetails?.city">
                    <label for="profileCity">City</label>
                </div>
            </div>
            <div class="col-sm-6">
                <img v-bind:src="'http://localhost:8000' + userDetails?.picture" height="350" width="350"
                    alt="Press 'View Profile'">

                <form method="POST" enctype="multipart/form-data" class="mt-2" @submit.prevent="updateUserPicture()">
                    <input type="file" accept="image/*" name="myFile" id="profileInput">
                    <input type="submit">
                </form>

            </div>
        </div>
        <div class="row">
            <div col-sm-6>
                <button @click="fetchUserDetails()">View profile</button>
            </div>
            <div col-sm-6>
                <button @click="updateUserDetails()" class="mt-2">Update profile</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
type User = {
    username: string;
    fname: string;
    sname: string;
    dob: string;
    city: string;
    email: string;
    id: string;
    picture: string;
};
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

// Adding local state
export default {
    data() {
        return {
            userDetails: null as null | User,
        }
    },
    mounted() {
        this.fetchUserDetails();
    },
    methods: {
        async updateUserDetails() {
            //Performs an Ajax PUT request to update a user's profile.
            let givenUser = document.getElementById("profileUsername") as HTMLInputElement
            let givenFname = document.getElementById("profileFirstName") as HTMLInputElement
            let givenSname = document.getElementById("profileSurname") as HTMLInputElement
            let givenDob = document.getElementById("profileDOB") as HTMLInputElement
            let givenCity = document.getElementById("profileCity") as HTMLInputElement
            let givenEmail = document.getElementById("profileEmail") as HTMLInputElement


            let response = await fetch("http://127.0.0.1:8000/api/users/" + this.userDetails?.id + "/", {
                method: 'PUT',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie("csrftoken")
                },
                body: JSON.stringify({
                    data: {
                        username: givenUser.value,
                        fname: givenFname.value,
                        sname: givenSname.value,
                        dob: new Date(givenDob.value).toISOString().split('T')[0],
                        city: givenCity.value,
                        email: givenEmail.value,
                    }
                })
            })
            let data = await response.json();
            this.fetchUserDetails();
        },

        async updateUserPicture() {
            const formData = new FormData()
            let fileField = document.querySelector("#profileInput") as HTMLInputElement;

            if (fileField.files && fileField.files.length > 0) {
                formData.append('myFile', fileField.files[0])
            }

            let response = await fetch("http://127.0.0.1:8000/api/profile/" + this.userDetails?.id + "/", {
                method: 'POST',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'X-CSRFToken': getCookie("csrftoken")
                },
                body: formData,
            })
            let data = await response.json();
        },

        async fetchUserDetails() {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            let data = await response.json();
            this.userDetails = data.User
        },
    }
}

import 'bootstrap/dist/css/bootstrap.css';

</script>
