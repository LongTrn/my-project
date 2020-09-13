import React, {useState} from 'react';

import '../styles/Table.input.css';

function TableInputs(props) {
    const [rows, setRows] = useState(2)
    const [cols, setCols] = useState(2)
    const [state, setState] = useState({
        listAttributes: [{attribute:'New Attribute'}]
    })
    let attr = []
    for (let i = 0; i < cols||props.cols; i++){
        attr.push(
            <td>{rows}</td>
        )
    }

    function addAttributes() { 
        let newAttr = (state.listAttributes)
        console.log(newAttr)
        setState((prevState) => ({
            ...prevState,
            listAttributes: [
                ...prevState.listAttributes,
                {attribute:'New Attribute'}
            ]
        }))

    }


    const { listAttributes } = state;
    return (
        <div className="Table.input">
            <table>
                <thead>
                    { 
                        listAttributes.length > 0 && listAttributes.map((item, index) => {
                            return <input key={index} type="text" placeholder={item.attribute}/>
                    })}
                    <input type="button" onClick={addAttributes} value='Attribute'/>
                </thead>
                {/* <tbody>
                    <tr>
                        {attr}
                    </tr>
                </tbody> */}
            </table>
        </div>
    );
}

export default TableInputs;
