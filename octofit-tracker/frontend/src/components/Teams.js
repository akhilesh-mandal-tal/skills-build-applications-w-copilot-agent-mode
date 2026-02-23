import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = `https://${codespaceName}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching teams from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map((team, idx) => (
          <li key={team.id || idx}>{team.name || JSON.stringify(team)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
