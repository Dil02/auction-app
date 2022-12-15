<template>
    <div>
        <h1>Questions And Answer</h1>
        <!-- Display All questions with the response -->

        <div v-for="q in questions" class="question border rounded  pb-3 mb-3 ml-2  me-5">
            <div>
                <h1 class="title">{{ q.title }}</h1>
                <h3>Question: {{ q.description }}</h3>
                <h3>Answer: {{ q.response }} </h3>
                <!-- OWNERID ==user ID IF THIS IS TRUE OUTPUT A BUTTON TO ADD ANSWER! -->
                <div v-if='ownerId == userId'>
                    <div v-if="q.response == '' || q.response == null">
                        <button @click="answerForm(q.id)">Add Answer</button>
                    </div>
                </div>

            </div>
        </div>
        <!-- IF USERID !=OWNER THEN HAVE A BUTTON TO POST A QUESTION (SMALL FORM BOOOM) -->
        <div v-if='ownerId!= userId'>
            <h2>Add Question</h2>
            <form v-on:submit.prevent="SaveQuestion">
                <div class="form-input">
                    <h3>
                        <label class="form-label" for="title">Title </label>
                        <input v-model="title" type="text" class="form-control" placeholder="Enter question title">
                    </h3>
                </div>
                <div class="form-input mb-2">
                    <h3><label for="Description">Description</label>
                        <textarea v-model="description" class="form-control" id="Desc" rows="4" required></textarea>
                    </h3>
                </div>
                <button type="submit" class="btn btn-primary mt-4 pt-2 w-50 mb-3" id="b">Submit</button>

            </form>
        </div>
    </div>
</template>


<script lang="ts">
function getCookie(name:any) {
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
            questions: [] as any[],
            userId: null,
            title: '',
            description: '',
            check: false,
            ownerId:null,

        }
    },
    methods: {
        async fetch_questions() {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id + "/questions", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" });  // NEED to add itemID so it can get all questions from a specific item  (need to add the view for it still)
            let data = await response.json();
            this.questions = data.questions;
            console.log("check" + this.questions)
        },
        //Gets The userID  THAT IS CURRENTLY LOGGED IN!-i dont know if we can current get the user id tho
        async fetch_user() {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            const data = await response.json();
            this.userId = data.User.id;
            this.ownerId=this.item.owner.id
            console.log("ITEM-OWNER-ID"+this.item.owner)
            console.log("the userID is"+this.userId)
        },
        async SaveQuestion(){
            const question = JSON.stringify({
                title: this.title,
                description: this.description,
                item: this.$route.params.id,
                response:'',
            })
                let response = await fetch("http://127.0.0.1:8000/api/questions/", {
                    method: 'POST',
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie("csrftoken"),
                    },
                body: question,
            })
        },
        async answerForm(id: any) {

            let response = await fetch("http://127.0.0.1:8000/api/questions/" + id + "/");


            //create Answer form

        },
        toggle() {
            this.check = !this.check
        },
    },
    async mounted() {
        this.fetch_user();
        this.fetch_questions();
    },
    updated(){
        console.log(this.item.owner);
    }
    
}
</script>

<style scoped>
.title{
    font-weight:bold;

    
}
.question{
    color:white;
    background-color:#312c2c;

}
</style>