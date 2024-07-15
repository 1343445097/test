import { useRoute,useRouter } from 'vue-router'
import axios from 'axios'
import { createStore } from 'vuex'
import { shallowRef } from 'vue'
import router from '../router'
import mymain from '../components/mymain.vue'
import myvideo from '../components/myvideo.vue'
import myalgorithm from '../components/myalgorithm.vue'
import mydeploy from '../components/mydeploy.vue'
import myvideiomanager from '../components/myvideoManager.vue'

const store = createStore({

    state:{
        username:'',
        is_login:false,
        baseUrl:"http://127.0.0.1:8000/",

        mainPage:shallowRef(mymain),
        
        myvideo_:{
            url:"http://127.0.0.1:80/live/test3.live.flv"
        }
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
        },
        
        switchPage(state,data){
            let pageid = data.pageid
            let url = data.url
            state.myvideo_.url = url
            if( pageid=='1-1'){
                state.mainPage = mymain
              }
              else if(pageid=='2-1')
              {
                state.mainPage = myvideiomanager
              }
              else if(pageid=='2-2')
              {
                state.mainPage = myvideo
              }
              else if(mpageid=='3-1')
              {
                state.mainPage = myalgorithm
              }
              else if(pageid=='4-1')
              {
                state.mainPage = mydeploy
              }
        }
    },

    actions:{

    },

    modules:{

    }

})


export default store;