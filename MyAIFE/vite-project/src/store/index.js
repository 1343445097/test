import { useRoute,useRouter } from 'vue-router'
import axios from 'axios'
import { createStore } from 'vuex'
import router from '../router'

const store = createStore({

    state:{
        username:'',
        is_login:false,
        baseUrl:"http://127.0.0.1:8000/"

    },

    getters:{

    },

    mutations:{
        updateUser(state,user){
            console.log("登录了",user)
            state.is_login = user.is_login
        },
        logout(state){
            state.is_login = false
            axios.get(state.baseUrl+"users/logout/",
                {user:state.username}
            
            ).then((res)=>{
                console.log("退出登录",res)
                console.log(router)
                router.replace("/login")
                localStorage.removeItem("token")
            }).catch((err)=>{
                console.log("退出失败",err)
            })
        }
    },

    actions:{

    },

    modules:{

    }

})


export default store;