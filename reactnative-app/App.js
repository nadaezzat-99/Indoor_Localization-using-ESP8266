import { StatusBar } from 'expo-status-bar';
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View,Image, Button ,ImageBackground} from 'react-native';
import { Dimensions } from 'react-native';
// import { Button } from 'react-native-web';
const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;
export default function App() {
  let [top,setTop]=useState(55)  //150
  let [left,setLeft]=useState(705)  //200
  let [sec,setSec]=useState(0)
  // let array_track= ["lecturesHall","hallWayOne","hallWayTwo",
  // "hallWayOne","hallWayTwo","hallWayOne","hallWayTwo","hallWayOne","lecturesHall",
  // "TA_Office","elec_lab","elec_lab","elec_lab","elec_lab","elec_lab","TA_Office"]
  let array_track=[]  //daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  // let label = "hallWayTwo_back"
  let label = ''
  let last_updated=[]
  setInterval(()=>{setSec(sec+=1)},5000)
  // let[loc,setLoc]=useState(0)
  //https://run.mocky.io/v3/f3441784-8f9c-49b4-a3a4-e7bf77cfeee6
  //http://172.28.129.147:8090/mapping
 async function locationHandler()
  {//http://127.0.0.1:5000/ SERVER
    let data= await fetch ("http://192.168.43.248:8090/mapping")
    let finalData=await data.json()
    console.log(finalData.label)
    // setLoc(finalData.labelone)
     label=finalData.label;
     console.log(label)
     array_track.push(label)  ////////daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    // console.log(array_track)
    // =========================//lecturesHall  LABEL (1)===================================================
    // if (label=="lecturesHall")   
    // {
    //   setTop(200);
    //   setLeft(250);
    // }
    // ===========================//hallWay1   LABEL  (2)===================================================
  // if(label =="hallWayOne")  
  //   {
  //     setTop(230);
  //     setLeft(850);
  //   }   
  // ===========================//hallWay2   LABEL  (3)===================================================
    // else if (label =="hallWayTwo")
    // {
    //   setTop(300);
    //   setLeft(850);
    // }
  // // ===========================//TA_Office   LABEL  (4)===================================================
  // else if (label =="TA_Office")
  // {
  //   setTop(300);
  //   setLeft(140);
  // }
  // ===========================//calib_lab  LABEL  (5)===================================================
  // else if (label =="calib_lab ")
  // {
  //   setTop(350);
  //   setLeft(910);
  // }
    // ===========================//network_lab  LABEL  (6)===================================================
  // else if (label =="network_lab")
  //   {
  //     setTop(400);
  //     setLeft(780);
  //   }
    // ===========================//elec_lab  LABEL  (7)===================================================
    if (label =="elec_lab")
      {
        setTop(410);
        setLeft(120);
      }
      // ===========================//hallWay3  LABEL  (8)===================================================
      else if (label =="hallWayOne_front")
      {
        setTop(350);
        setLeft(190);
      }
      else if (label =="hallWayOne_back")
      {
        setTop(550);
        setLeft(190);
      }
      else if (label =="hallWayTwo_front")
      {
        setTop(250);
        setLeft(120);
      }
      else if (label =="hallWayTwo_back")
      {
        setTop(250);
        setLeft(250);
      }

  }
  if (array_track.length>53)
  {
    last_updated= array_track.slice(2,51)
  }

  function track_mode()
  {
    console.log(last_updated)
    console.log("track")
   let track_history= last_updated.pop()

   console.log("track_history",track_history)
    console.log("arraytrack",last_updated)
    // =========================//lecturesHall  LABEL (1)===================================================
    if (track_history =="elec_lab")
      {
        setTop(410);
        setLeft(120);
      }
      // ===========================//hallWay3  track_history  (8)===================================================
      else if (track_history =="hallWayOne_front")
      {
        setTop(350);
        setLeft(190);
      }
      else if (track_history =="hallWayOne_back")
      {
        setTop(550);
        setLeft(190);
      }
      else if (track_history =="hallWayTwo_front")
      {
        setTop(250);
        setLeft(120);
      }
      else if (track_history =="hallWayTwo_back")
      {
        setTop(250);
        setLeft(250);
      }
      else if(last_updated.length=="")
      {
          return
      }

      setTimeout(()=>{track_mode()},500)

    }
  useEffect(()=>locationHandler(),[sec])
  return (
  
    <View  style={styles.container}>
      {/* <Image style={styles.logo} source={require('./assets/logo.jpg')}/> */}
      <Text style={styles.title}> Indoor Localization Of SBME Department</Text>
      <Image 
        style={styles.image}
        source={require('./assets/SBMEMAP.png')}
      />        
       <Image style={{position:"absolute",top:top,left:left,width:25,height:30,padding:10}} source={require('./assets/logoo.jpg')}/>
      <Button  onPress={()=>{track_mode()}} title="Tracking Mode"> </Button>
   
        </View>

    

  );
}

const styles = StyleSheet.create({
  container: {
    // width:windowWidth,
    // height:windowHeight,
    flex: 1,
    backgroundColor: '#EEEDDE',
    alignItems: 'center',
    justifyContent: 'center',
    
  },
  image:
  {
    //display:"flex",
    justifyContent:"center",
    alignItems:"center",
    width:300,  //300
    height:550 , ///700
    // transform: [{ rotate: '90deg' }]
  },
  // CircleShape: {
  //   position:"absolute",
  //   top:top,
  //   left:left,
  //   width: 10,
  //   height: 10,
  //   borderRadius: 10 / 2,
  //   backgroundColor: 'red',
  //   opacity:0.6,
  // },
  title:
  {
    fontSize: 20,
    fontWeight: "bold",
    // fontFamily: 'Cochin',
    marginBottom:10,
    marginTop:10,
    // backgroundColor:'rgba(1,1,1,0.7)'
  },
  logo:
  {
    width:25,
    height:30,
    padding:10

  }
});
