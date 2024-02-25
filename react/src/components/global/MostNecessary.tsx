import axios from "axios";
import { useEffect, useState } from "react";

interface NecessaryData {
    blood_group: { title: string };
    rhesus: { title: string };
    pet_type: { title: string
        icon: string; };
  }

const MostNecessary = () => {
    const [necessary, setNecessary] = useState<NecessaryData | undefined>();
    const [min, setMin] = useState<NecessaryData | undefined>();

    useEffect(() => {
        axios.get('blood_bank/necessary').then((response) => {
            setNecessary(response.data);
            console.log(response.data);
          });
          axios.get('blood_bank/min').then((response) => {
            setMin(response.data);
            console.log(response.data);
          });
        console.log(necessary);
        console.log(min);
        }, [])

        if (!necessary || !min) {
            return <div></div>;
          }

    return(
    <div style={{ 'marginBottom' : '30px'}}> 
      <div style={{display: 'flex',
      }}>
        <div  style={{'marginRight': '10px'
      }}>Наиболее востребованная кровь:</div>
        <div  style={{'marginRight': '10px'
      }}>{necessary.blood_group.title},</div>
        <div  style={{'marginRight': '10px'
      }}>{necessary.rhesus.title}</div>
        <div  style={{'marginRight': '10px'
      }}>{necessary.pet_type.title}</div>
        <img style={{
                          width: 20,
                          height: 20,
                          marginRight: 5,
                        }} src={necessary.pet_type.icon} alt="#" />
        </div>
        <div style={{display: 'flex'
      }}>
         <div style={{'marginRight': '10px'
      }}>Кровь, которой меньше всего:</div>
        <div style={{'marginRight': '10px'
      }}>{min.blood_group.title},</div>
        <div style={{'marginRight': '10px'
      }}>{min.rhesus.title}</div>
        <div  style={{'marginRight': '10px'
      }}>{min.pet_type.title}</div>
        <img style={{
                          width: 20,
                          height: 20,
                          marginRight: 5,
                        }} src={min.pet_type.icon} alt="#" />
                        </div>
    </div>)
}

export default MostNecessary;