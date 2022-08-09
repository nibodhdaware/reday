import React, { useState } from "react";
import Calendar from "react-calendar";
import styles from "../styles/Sidebar.module.css";

export default function Sidebar() {
    const [date, setDate] = useState(new Date());

    const onChange = (date) => {
        setDate(date);
    };

    return (
        <div className={styles.container}>
            <Calendar onChange={onChange} value={date} />
        </div>
    );
}
