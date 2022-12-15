<template>
    <div>
        <h1>Questions And Answer</h1>
        <!-- Display All questions with the response -->
        This {{ownerId}}
        <div v-for="(q,index) in questions" class="question border rounded  pb-3 mb-3 ml-2  me-5" :key="index">
            <div>
                <h3 class="title">{{ q.title }}</h3>
                <h5>Question: {{ q.description }}</h5>
                <h5>Answer: {{ q.response }} </h5>
                <!-- OWNERID ==user ID IF THIS IS TRUE OUTPUT A BUTTON TO ADD ANSWER! -->
                <div v-show='(check==false)'>
                    <div v-if="q.response == '' || q.response == null">
                        <button @click="answerForm($event,q.id)" >Add Answer</button>
                        <form v-on:submit.prevent="updateQuestion(q.id)"  >
                            <textarea v-model="response[index]" class="form-control w-75 ml-auto mx-auto"  rows="4" ></textarea>
                            <button type="submit" class="btn btn-primary  pt-2 w-50 mb-2 ml-auto mx-auto mt-2" id="c" >Submit</button>
                         </form>
                    </div>
                </div>

            </div>
        </div>
        <!-- IF USERID !=OWNER THEN HAVE A BUTTON TO POST A QUESTION (SMALL FORM BOOOM) -->
        {{check}}
        <div v-if="check">
            <form v-on:submit.prevent="SaveQuestion" class="sq d-flex flex-column justify-content-center mx-auto w-50">
                <h2>Add Question</h2>
                <div class="form-input">
                    <h3>
                        <label class="form-label" for="title">Title</label>
                        <input v-model="title" type="text" class="form-control w-100" placeholder="Enter question title">
                    </h3>
                </div>
                <div class="form-input mb-2">
                    <h3><label for="Description">Description</label>
                        <textarea v-model="description" class="form-control" id="Desc" rows="4" required></textarea>
                    </h3>
                </div>
                <button type="submit" class="btn btn-primary  pt-2 w-50 mb-3 mx-auto" id="b" >Submit</button>

                
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
    data() {
        return {
            questions: [] as any[],
            userId: null,
            title: '',
            description: '',
            check: false,
            ownerId:null,
            valid:true,
            valid2:false,
            response:[],
            item:null,
        }
    },
    methods: {

       async fetch_item(){
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id);
            let data = await response.json();
            this.item=data.item;   
            this.ownerId=data.item.owner.id;  
        },
        async fetch_questions() {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id + "/questions", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" });  // NEED to add itemID so it can get all questions from a specific item  (need to add the view for it still)
            let data = await response.json();
            this.questions = data.questions;
        },
        //Gets The userID  THAT IS CURRENTLY LOGGED IN!
        async fetch_user() {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            const data = await response.json();
            this.userId = data.User.id;
            console.log(this.item)
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
            this.fetch_questions();
        },
        async answerForm(event:any,id: any) {
            
            const button = event.target;
            button.style.display = 'none';

            console.log(id)
            
            //create Answer form

        },

        async updateQuestion(id:any){
            const question = JSON.stringify({
                title: this.title,
                description: this.description,
                item: this.$route.params.id,
                response:this.response,
            })
            console.log("id")
            let response = await fetch("http://127.0.0.1:8000/api/questions/"+id+"/", {
                    method: 'PUT',
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
        toggle() {
            this.check = !this.check
        },
    },
    async mounted() {
        this.fetch_item();
        this.fetch_user();
        this.fetch_questions();
    },
    computed: {
        check: function() {
            console.log("C "+this.userId)
            console.log("C "+this.ownerId)
            if (this.userId ==this.ownerId) {
                return false;
            }
            return true
  },
 
}
    
}
</script>

<style scoped>
.title{
    font-weight:bold;
    color:rgb(30, 166, 251);

    
}
.question{
    color:white;
    background-color:#312c2c;

}
.sq{
    color:white;
    background-color:#312c2c;
    border-radius: 3%;
    margin-bottom: 2%;
}
</style>