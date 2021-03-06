from .api import API, Group


class Groups(API):

    def __init__(self):
        super().__init__()
        self._domain = f'{self._domain}/groups'

    def get(self, status: str = 'active', group_id: int = None, ) -> list:

        """Retrieves all groups (or a specific group if a group_id is provided) in your KnowBe4 account

        :parameter status: a str, Filter results based on status (active / archived) [Default = active]
        :parameter group_id: a str, A group ID to filter on
        :return: a list, API response(s)
        :rtype: list
        """

        params = {}

        # Get a Specific Group
        # https://developer.knowbe4.com/reporting/#tag/Groups/paths/~1v1~1groups~1{group_id}/get
        if group_id:
            return [Group.from_dict(group)
                    for group in self._request(method="GET", url=f'{group_id}')]

        # Get All Groups:
        # https://developer.knowbe4.com/reporting/#tag/Groups/paths/~1v1~1groups/get
        else:
            if group_id:
                params.update({'group_id': group_id})
            if status.lower() not in ['archived', 'active']:
                raise ValueError(f'{status} is an invalid value for status. Possible values: '
                                 f'["active", "archived"]')
            else:
                if status.lower() == 'archived':
                    params.update({'status': 'archived'})
                elif status.lower() == 'active':
                    params.update({'status': 'active'})

            return [Group.from_dict(group)
                    for group in self._request(method="GET", url="", params=params)]
