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
                        v-model="username">
                    <label for="profileUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Clyde" id="profileFirstName"
                        v-model="fname">
                    <label for="profileFirstName">First Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="Tyler" id="profileSurname"
                        v-model="sname">
                    <label for="profileSurname">Surname</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="name@example.com" id="profileEmail"
                        v-model="email">
                    <label for="profileEmail">Email Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="01/01/2000" id="profileDOB"
                        v-model="dob">
                    <label for="profileDOB">Date of Birth</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control bg-light" placeholder="London" id="profileCity"
                        v-model="city">
                    <label for="profileCity">City</label>
                </div>
            </div>
            <div class="col-sm-6">
                <img v-bind:src="'http://localhost:8000' + picture" height="350" width="350" alt="Press 'View Profile'">

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

    <p class="errorMsg bold" v-if="invalidInput">Error occurred. Please check your inputs.</p>
    <p class="successMsg bold" v-if="validInput">Your profile has been successfully updated.</p>

</template>

<script lang="ts">

function getCookie(name: String): string {
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
            username: null as null | string,
            fname: null as null | string,
            sname: null as null | string,
            dob: null as null | string,
            city: null as null | string,
            email: null as null | string,
            id: null as null | string,
            picture: null as null | string,
            invalidInput: false,
            validInput: false,
        }
    },
    mounted(): void {
        this.fetchUserDetails();
    },
    methods: {
        async updateUserDetails(): Promise<void> {
            //Performs an Ajax PUT request to update a user's profile.
            let givenUser = document.getElementById("profileUsername") as HTMLInputElement
            let givenFname = document.getElementById("profileFirstName") as HTMLInputElement
            let givenSname = document.getElementById("profileSurname") as HTMLInputElement
            let givenDob = document.getElementById("profileDOB") as HTMLInputElement
            let givenCity = document.getElementById("profileCity") as HTMLInputElement
            let givenEmail = document.getElementById("profileEmail") as HTMLInputElement


            let response = await fetch("http://127.0.0.1:8000/api/users/" + this.id + "/", {
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
            this.validInput = true;
            this.invalidInput = false;
            this.fetchUserDetails();
        },

        async updateUserPicture(): Promise<void> {
            const formData = new FormData()
            let fileField = document.querySelector("#profileInput") as HTMLInputElement;

            if (fileField.files && fileField.files.length > 0) {
                formData.append('myFile', fileField.files[0])
            }

            let response = await fetch("http://127.0.0.1:8000/api/profile/" + this.id + "/", {
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
            this.validInput = true;
            this.invalidInput = false;
            this.fetchUserDetails();

        },

        async fetchUserDetails(): Promise<void> {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            let data = await response.json();
            let record = data.User
            this.username = record.username;
            this.fname = record.fname;
            this.sname = record.sname;
            this.dob = record.dob;
            this.city = record.city;
            this.email = record.email;
            this.id = record.id;
            this.picture = record.picture;

        },
    }
}

import 'bootstrap/dist/css/bootstrap.css';

</script>

<style>
.errorMsg {
    color: red;
}

.successMsg {
    color: green;
}

.bold {
    font-weight: bolder;
    text-align: center;
}
</style>