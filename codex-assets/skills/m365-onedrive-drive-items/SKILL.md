---
name: m365-onedrive-drive-items
description: >-
  Upload, download, share, and traverse OneDrive/SharePoint files via driveItem endpoints and upload sessions — when moving files programmatically
---

# m365-onedrive-drive-items

Address files two ways: by id `/drives/{driveId}/items/{itemId}` or by path `/drives/{driveId}/root:/Reports/q2.pdf:`. Download bytes: `GET .../items/{id}/content` (302-redirects to a pre-authed download URL). Simple upload (<4MB): `PUT .../root:/path/file.txt:/content` with raw body. List a folder: `GET .../root/children` or `.../items/{id}/children`.

**Large files** need a resumable upload session: `POST .../root:/big.zip:/createUploadSession`, then `PUT` byte ranges to the returned `uploadUrl` with `Content-Range: bytes 0-327679/2000000`, ~320KB-aligned chunks.

Share: `POST .../items/{id}/createLink` `{"type":"view","scope":"organization"}`.

Pitfall: the path-addressing colon syntax is finicky — the trailing `:` after the path and before `/children` is required; `root:/folder:/children` works, `root:/folder/children` does not. Pitfall 2: upload chunks must be exact multiples of 320KB except the final chunk, and `Content-Range` is inclusive byte indices. Pitfall 3: `/content` on a folder errors; check `folder` vs `file` facet first.

**Tools:** /drive/root:/path, /content, createUploadSession, /createLink, driveItem
